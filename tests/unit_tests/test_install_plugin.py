import unreal
import moderlab

from automation_test.unittest_utilities import *

runner = TestRunner()


@runner.set_before_all
def setup():
    print('Hello World Setup')


@runner.set_after_all
def tear_down():
    print('Reset test value')


@runner.set_after_each
def after():
    print('Test after')


@test_on_win
@runner.add_test
def get_moderlab_pipeline_response():
    print('!! look moderlab pipeline work')
    pipeline = moderlab.ModerApp()
    unreal.log_warning(pipeline.get_response())
    unreal.log_error('!! Failed to make this test')
    exit(1)


if __name__ == '__main__':
    runner.run_all()
