import torch
from transformers import GPT2Model

# Load the GPT-2 model
model = GPT2Model.from_pretrained("gpt2")
model.eval()  # Set to evaluation mode

# Create a dummy input tensor
dummy_input = torch.randint(0, 1000, (1, 10))

# Export to ONNX
torch.onnx.export(
    model, dummy_input, "gpt2.onnx",
    input_names=["input"],
    output_names=["output"],
    dynamic_axes={"input": {0: "batch_size"}, "output": {0: "batch_size"}}
)

print("Model successfully exported to ONNX format: gpt2.onnx")