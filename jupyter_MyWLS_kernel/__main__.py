from ipykernel.kernelapp import IPKernelApp
from .kernel import WLScriptKernel
IPKernelApp.launch_instance(kernel_class=WLScriptKernel)
