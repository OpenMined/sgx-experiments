# SGX Experiments
Trusted execution experiments with Intel SGX

## Getting Started

To run the experiments on this repository, make sure you have installed the Intel SGX SDK and driver.  

Download and install them from the official Intel GitHub repositories:

- https://github.com/01org/linux-sgx
- https://github.com/01org/linux-sgx-driver

Alternatively, if you want to use the DCAP versions of the SDK and driver, download and install it from:
- https://github.com/intel/SGXDataCenterAttestationPrimitives

## Experiments

### Graphene SGX

Graphene is a lightweight guest OS, designed to run a single application with minimal host requirements. Graphene can run applications in an isolated environment with benefits comparable to running a complete OS in a virtual machine - including guest customization, ease of porting to different OSes, and process migration.

Graphene supports native, unmodified Linux applications on any platform. Currently, Graphene runs on Linux and Intel SGX enclaves on Linux platforms.
With Intel SGX support, Graphene can secure a critical application in a hardware-encrypted memory region. Graphene can protect applications from a malicious system stack with minimal porting effort.

#### Proofs of concept
- [PyTorch with SGX: Image Classification](./graphene/pytorch)
- [PySyft with SGX: Secure Aggregation](./graphene/pysyft)

#### Useful Links
- Paper: http://www.cs.unc.edu/~porter/pubs/tsai14graphene.pdf
- Website: https://grapheneproject.io/

## Support
For support in using this library, please join the **#lib_sgx-experiments** Slack channel. If you’d like to follow along with any code changes to the library, please join the **#code_sgx-experiments** Slack channel. [Click here to join our Slack community!](https://slack.openmined.org)
