import argparse
from src.data import load_data
from src.models import train_model
from src.visualization import visualize_results

def main(args):
    # Load and preprocess data
    data = load_data(args.data_path)
    
    # Train model
    model = train_model(data)
    
    # Visualize results
    visualize_results(model, data)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Cancer Detection AI")
    parser.add_argument("--data_path", type=str, required=True, help="Path to the dataset")
    args = parser.parse_args()
    main(args)