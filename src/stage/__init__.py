
import demo_stage

__stages = {
    "demo1" : demo_stage.DemoStage,
}

def load_stage(name):
    return __stages[name]()
