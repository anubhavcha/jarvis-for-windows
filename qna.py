from listen import Listen
from speak import speak
def load_qa_data(file_path):
    qa_dict = {}
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(":")
            if len(parts) != 2:
                print(f"Skipping line: {line}")
                continue
            q, a = parts
            qa_dict[q] = a
    return qa_dict





