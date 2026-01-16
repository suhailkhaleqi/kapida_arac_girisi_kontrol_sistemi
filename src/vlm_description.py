import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
).to(DEVICE)


def describe_vehicle(pil_image: Image.Image) -> str:
    """
    Generate a natural language description of the vehicle image.
    """

    inputs = processor(
        pil_image,
        return_tensors="pt"
    ).to(DEVICE)

    outputs = model.generate(
        **inputs,
        max_length=40
    )

    description = processor.decode(
        outputs[0],
        skip_special_tokens=True
    )

    return description
