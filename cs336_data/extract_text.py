from resiliparse.parse.encoding import detect_encoding
from resiliparse.extract.html2text import extract_plain_text


def extract_text_from_html_bytes(html_bytes):
    try:
        html_str = html_bytes.decode('utf-8')
    except UnicodeDecodeError:
        encoding = detect_encoding(html_bytes)
        html_str = html_bytes.decode(encoding, errors='replace')

    return extract_plain_text(html_str)

# just run the text extraction function on a single WARC file to compare the output
# to the extracted text in the corresping WET file. And see the difference 
if __name__ == "__main__":
    import gzip
    from fastwarc.warc import ArchiveIterator, WarcRecordType

    warc_path = "/Users/huhuaxiao/Documents/GitHub/cs336-assignment4-data/data/CC/example.warc.gz"
    count = 0
    with gzip.open(warc_path, 'rb') as f:
        for record in ArchiveIterator(f):
            if record.record_type == WarcRecordType.response and record.content_length > 0:
                html_bytes = record.reader.read()
                text = extract_text_from_html_bytes(html_bytes)
                print(text)
                print("--------------------------------------------------")
                count += 1
                if count >= 10:
                    break