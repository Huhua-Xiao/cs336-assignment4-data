import fasttext
import re

from cs336_data.extract_text import extract_text_from_html_bytes
from cs336_data.language_identification import identify_language
from cs336_data.mask_pii import mask_emails, mask_phone, mask_ip
from cs336_data.harmful_content import identify_nsfw, identify_toxic_speech
from cs336_data.gopher_quality_filters import gopher_quality_filter

import gzip
from fastwarc.warc import ArchiveIterator, WarcRecordType

input_path = "/Users/huhuaxiao/Documents/GitHub/cs336-assignment4-data/data/wiki/subsampled_positive_urls.warc.gz"
output_path = "/Users/huhuaxiao/Documents/GitHub/cs336-assignment4-data/data/wiki/subsampled_positive_urls.txt"


def clean_text_basic(text: str): 
    text = text.replace("\n", " ").replace("\r", " ")
    text = re.sub(r"\s+", " ", text)
    return text.strip()

def query_positive_sample():
    samples = []
    with gzip.open(input_path, 'rb') as f:
        for record in ArchiveIterator(f):
            if record.record_type == WarcRecordType.response and record.content_length > 0:
                html_bytes = record.reader.read()
                text = extract_text_from_html_bytes(html_bytes)
                lang, lang_conf = identify_language(text)
                
                if lang != "en" or lang_conf < 0.5:
                    continue # skip non-English or low confidence

                nsfw_label, nsfw_conf = identify_nsfw(text)
                if nsfw_label == "NSFW" and nsfw_conf >= 0.7:
                    continue # skip NSFW content
                toxic_label, toxic_conf = identify_toxic_speech(text)
                if toxic_label == "TOXIC" and toxic_conf >= 0.7:
                    continue # skip toxic content
                if not gopher_quality_filter(text):
                    continue # skip low-quality content

                text = clean_text_basic(text)
                text = mask_emails(mask_phone(mask_ip(text)[0])[0])[0]
                if not text: continue

                samples.append(f"__label__positive {text}\n")


    with open(output_path, "wt", encoding="utf-8") as f_out:
        f_out.writelines(samples)
    
    print (f"Written {len(samples)} positive samples to {output_path}")

if __name__ == "__main__":
    query_positive_sample()
    