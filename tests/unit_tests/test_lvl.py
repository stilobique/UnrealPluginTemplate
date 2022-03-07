import unreal


@unreal.AutomationScheduler.add_latent_command
def setup_test_level():
    unreal.log("SETUP TEST LEVEL")


@unreal.AutomationScheduler.add_latent_command
def test_level():
    # test level
    unreal.log("TEST LEVEL")


@unreal.AutomationScheduler.add_latent_command
def post_test_level():
    unreal.log("POST TEST LEVEL")
    unreal.log_error('Failed to make this test')
    exit(1)
