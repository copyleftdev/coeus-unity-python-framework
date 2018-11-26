import coeus.message

DEFAULT_TIMEOUT_SECONDS = 60
DEFAULT_TRANSFORM_EXISTS = True
DEFAULT_RENDERER_VISIBLE = True
DEFAULT_SCENE_LOADED = True


def query_transform_exists(cli, transform_path):
    """
    Requests status on whether a transform exists or not.
    :param cli:
    :param transform_path:
    :return:
    """

    message_payload = {
        "transform_path": transform_path
    }
    msg = coeus.message.Message("query.unity.transform.exists", message_payload)
    cli.send_message(msg)


def await_transform_exists(cli, transform_path, does_exist=DEFAULT_TRANSFORM_EXISTS, timeout_seconds=DEFAULT_TIMEOUT_SECONDS):
    """
    Waits for a transform to exist based on does_exist.
    :param cli:
    :param transform_path:
    :param does_exist: Whether or not to await for exist state (True | False)
    :param timeout_seconds: How long until this returns with failure
    :return:
    """
    message_payload = {
        "transform_path": transform_path,
        "does_exist": does_exist,
        "timeout": timeout_seconds
    }
    msg = coeus.message.Message("await.unity.transform.exists", message_payload)
    cli.send_message(msg)
    return cli.read_message()


def query_transform_screen_position(cli, transform_path):
    """
    Requests screen position of a transform at path. WorldToScreenPoint is used for 3D, otherwise
    a screen-scaled center of RectTransform is used.
    :param cli:
    :param transform_path:
    :return:
    """

    message_payload = {
        "transform_path": transform_path
    }
    msg = coeus.message.Message("query.unity.transform.screenPosition", message_payload)
    cli.send_message(msg)


def query_renderer_visible(cli, transform_path):
    """
    Requests status on whether a renderer at transform_path is visible.
    :param cli:
    :param transform_path:
    :return:
    """

    message_payload = {
        "transform_path": transform_path
    }
    msg = coeus.message.Message("query.unity.renderer.visible", message_payload)
    cli.send_message(msg)


def await_renderer_visible(cli, transform_path, is_visible=DEFAULT_RENDERER_VISIBLE, timeout_seconds=DEFAULT_TIMEOUT_SECONDS):
    """
    Waits for a transform renderer to become visible based on is_visible.
    :param cli:
    :param transform_path:
    :param is_visible: Whether or not to await for visible state (True | False)
    :param timeout_seconds: How long until this returns with failure
    :return:
    """
    message_payload = {
        "transform_path": transform_path,
        "is_visible": is_visible,
        "timeout": timeout_seconds
    }
    msg = coeus.message.Message("await.unity.renderer.visible", message_payload)
    cli.send_message(msg)
    return cli.read_message()


def query_scene_loaded(cli, scene_name):
    """
    Requests status on whether a scene is loaded or not.
    :param cli:
    :param scene_name:
    :return:
    """

    message_payload = {
        "scene_name": scene_name
    }
    msg = coeus.message.Message("query.unity.scene.loaded", message_payload)
    cli.send_message(msg)


def await_scene_loaded(cli, scene_name, is_loaded=DEFAULT_SCENE_LOADED, timeout_seconds=DEFAULT_TIMEOUT_SECONDS):
    """
    Waits for a scene to be loaded based on is_loaded.
    :param cli:
    :param scene_name:
    :param is_loaded: Whether or not to await for loaded state (True | False)
    :param timeout_seconds: How long until this returns with failure
    :return:
    """
    message_payload = {
        "scene_name": scene_name,
        "is_loaded": is_loaded,
        "timeout": timeout_seconds
    }
    msg = coeus.message.Message("await.unity.scene.loaded", message_payload)
    cli.send_message(msg)
    return cli.read_message()