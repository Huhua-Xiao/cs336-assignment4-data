import os
import random

input_path = "/Users/huhuaxiao/Documents/GitHub/cs336-assignment4-data/data/wiki/enwiki-20240420-extracted_urls.txt"
output_path = "/Users/huhuaxiao/Documents/GitHub/cs336-assignment4-data/data/wiki/subsampled_positive_urls.txt"

def generate_sample_positive_quality_test(max_urls: int = 100000):
    random.seed(42) # for reproducibility

    # if the file size is less than 200MB, read all lines into memory
    if os.path.getsize(input_path) < 200 * 1024 * 1024:
        with open(input_path, "rt", encoding="utf-8", errors="ignore") as f:
            lines = [ln.strip() for ln in f if ln.strip()]
        sampled = random.sample(lines, min(max_urls, len(lines)))
        print("The input file is small enough, read all lines into memory.")
    else:
        reservoir = []
        with open(input_path, "rt", encoding="utf-8", errors="ignore") as  f:
            for i, line in enumerate(f):
                url = line.strip()
                if not url: continue
                if len(reservoir) < max_urls:
                    reservoir.append(url)
                else:
                    j = random.randint(0, i)
                    if j < max_urls:
                        reservoir[j] = url
        sampled = reservoir
    
    with open(output_path, "wt", encoding="utf-8") as f_out:
        for url in sampled:
            f_out.write(url + "\n")
        return len(sampled)

if __name__ == "__main__":
    num_sampled = generate_sample_positive_quality_test(100000)
    print(f"Sampled {num_sampled} positive quality URLs to {output_path}")