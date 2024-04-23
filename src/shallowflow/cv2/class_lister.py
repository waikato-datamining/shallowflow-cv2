from typing import List, Dict


def list_classes() -> Dict[str, List[str]]:
    return {
        "shallowflow.api.actor.Actor": [
            "shallowflow.cv2.sinks",
            "shallowflow.cv2.sources",
            "shallowflow.cv2.transformers",
        ],
        "shallowflow.base.conversions.AbstractConversion": [
            "shallowflow.cv2.conversions",
        ],
    }
