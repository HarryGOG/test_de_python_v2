import os
import inspect
import importlib
from luigi import interface as luigi_interface
import luigi.configuration as configuration
import sys

try:
    import luigi.configuration.core as configuration_core

    _parsers = configuration_core.PARSERS.values()
    _get_config_instance = configuration_core.get_config
except ImportError:
    from luigi.configuration import LuigiConfigParser as configuration_core

    _parsers = [configuration_core]
    _get_config_instance = configuration_core.instance


def add_class_setup_and_teardown(test_class, setup=None, teardown=None):
    """ Set given class setup method and teardown method to a specified TestCase class

    Parameters
    ----------
    test_class: type
        subclass of unittest.TestCase class
    setup:
        class setup function to be added
    teardown
        class teardown function to be added

    Returns
    -------
    type
        Extended class

    """
    _setUpClass = test_class.setUpClass
    _tearDownClass = test_class.tearDownClass

    @classmethod
    def setUpClass(cls):
        setup(cls)
        _setUpClass()

    @classmethod
    def tearDownClass(cls):
        _tearDownClass()
        teardown(cls)

    if setup:
        test_class.setUpClass = setUpClass

    if teardown:
        test_class.tearDownClass = tearDownClass

    return test_class



def with_luigi_config(config_path):
    """ Execute ``unittest.TestCase`` class with the specified Luigi configuration file.

    When a ``TestCase`` class with this decorator is executed, the specified Luigi configuration
    file is set to Luigi before ``setUpClass`` method is called.

    After execution of the ``TestCase`` class, the Luigi configuration file is removed from Luigi
    after ``tearDownClass`` method is called.


    Examples
    --------
    Run ``LuigiWorkflowTest`` class with Luigi configuration declared in ``tests/test_workflow.cfg``::

        @with_luigi_config("test_workflow.cfg")
        class LuigiWorkflowTest(TestCase):

    Parameters
    ----------
    config_path: str
        Relative path to the configuration file to use
    """

    def resolve_config_path(cls):
        return os.path.abspath(os.path.join(os.path.dirname(inspect.getfile(cls)), config_path))

    def set_config(cls):
        config_path_abs = resolve_config_path(cls)

        if not os.path.exists(config_path_abs):
            raise ValueError("Luigi configuration file was not found: {}".format(config_path_abs))

        configuration_core.add_config_path(config_path_abs)
        init_luigi_logging()

    def remove_config(cls):
        config_path_abs = resolve_config_path(cls)
        for p in _parsers:
            config_paths = p._config_paths
            if config_path_abs in config_paths:
                config_paths.remove(config_path_abs)
                p.reload()

    def decorate(cls):
        return add_class_setup_and_teardown(test_class=cls, setup=set_config, teardown=remove_config)

    return decorate


def init_luigi_logging():
    """ Initialize loggers with Luigi's logging configuration """
    env_params = luigi_interface.core()

    try:
        # Since Luigi 2.8.1
        setup_logging = importlib.import_module('luigi.setup_logging')
        setup_logging.InterfaceLogging._configured = False
        setup_logging.InterfaceLogging.setup(env_params)
        return
    except ImportError:
        pass

    if hasattr(luigi_interface, 'setup_interface_logging'):
        # Before Luigi 2.8.1
        logging_conf = env_params.logging_conf_file
        if logging_conf != '' and not os.path.exists(logging_conf):
            raise Exception(
                "Error: Unable to locate specified logging configuration file!"
            )

        if not configuration.get_config().getboolean(
                'core', 'no_configure_logging', False):
            luigi_interface.setup_interface_logging(logging_conf, env_params.log_level)
    else:
        # Otherwise
        sys.stderr.write("Cannot configure logger.")

