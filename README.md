# FastAPI ML Deployment Template

This repository provides a complete example of serving a machine learning model with FastAPI, containerizing it using Docker, and deploying it on Kubernetes.

## 🧠 Features

- ✅ FastAPI app with `/predict` endpoint
- ✅ Real scikit-learn model (Iris dataset)
- ✅ Lightweight Dockerfile with best practices
- ✅ Kubernetes manifests: Deployment, Service, HPA, Ingress
- ✅ Ready for production and educational use

## 📖 Related Medium Articles

- Part 1: [Serving ML Models with FastAPI](https://grigorkh.medium.com/serving-ml-models-with-fastapi-a-production-ready-api-in-minutes-b5f4839a33a9)
- Part 2: [Dockerizing Your FastAPI ML App - Comming Soon](https://grigorkh.medium.com/)
- Part 3: [Deploying Your ML API on Kubernetes - Comming Soon](https://grigorkh.medium.com/)

## 🚀 Quickstart

1. Clone the repo:
   ```
   git clone https://github.com/your-username/fastapi-ml-deployment-template.git
   ```

2. Train the model:
   ```
   python model/train_model.py
   ```

3. Build the Docker image:
   ```
   docker build -t your-dockerhub-username/fastapi-ml:latest .
   ```

4. Push it to Docker Hub (detailed guide coming soon).

5. Apply Kubernetes manifests:
   ```
   kubectl apply -f k8s/
   ```

6. Test the endpoint:
   ```
   curl -X POST http://localhost:8000/predict -H "Content-Type: application/json" -d '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'
   ```

---

## 📄 License

MIT
