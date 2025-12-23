import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="app.log"
)

def add(a, b):
    logging.info(f"Adding {a} and {b}")
    return a + b

def subtract(a, b):
    logging.info(f"Subtracting {b} from {a}")
    return a - b

def multiply(a, b):
    logging.info(f"Multiplying {a} and {b}")
    return a * b

def divide(a, b):
    if b == 0:
        logging.error("Division by zero attempted")
        return "Error"
    logging.info(f"Dividing {a} by {b}")
    return a / b

if __name__ == "__main__":
    logging.info("Calculator Application Started")
    print("Calculator App Running")


