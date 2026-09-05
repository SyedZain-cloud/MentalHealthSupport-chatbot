# Troubleshooting

## Adapter activation warning

The adapters library may print: `There are adapters available but none are
activated for the forward pass.` The deployed forward method explicitly calls
the RoBERTa encoder path used during training. The packaged offline loader was
numerically compared with the original research-project loader and produced
identical probabilities. The warning does not indicate a checkpoint mismatch.

## Out of memory

The checkpoint is large. Close other GPU applications, use `device="cpu"`, or
run the model as one shared API service instead of loading a copy per user.

## Slow responses

Do not construct `MercuryPredictor` inside a request handler. Construct it once
at application startup. CUDA is strongly recommended for interactive use.

## Missing package or incompatible PyTorch wheel

Install a PyTorch build appropriate for the machine and its CUDA driver, then
install the remaining pinned packages. The original verified environment used
Python 3.14.6 and PyTorch 2.13.0+cu130, but another compatible PyTorch build may
be required on the partner machine.
