# Overview
This repository contains the code example from [Deploy Sci-kit Learn models in .NET Core Applications](https://medium.com/@novackgm/deploy-sci-kit-learn-models-in-net-core-applications-90e24e572f64)

# Running locally
## Training
- From the /training directory, run `pip install -r requirements.txt` to install the required packages
- Run `python train.py` to build and train the model

## Inference
The ASP.NET Core inference application can be run either via the the dotnet Command-line tools, or via Docker
- Using the dotnet Command-line tools:
  - From the /inference directory, run `dotnet run`
- Using Docker 
  - From the /inference directory, run `docker build -t sklearn-dotnet .`
  - Run `docker run -p 80:80 sklearn-dotnet`
