from __future__ import annotations

import os
import fasttext
from typing import Any
from cs336_data.extract_text import extract_text_from_html_bytes
from cs336_data.language_identification import identify_language
from cs336_data.mask_pii import mask_emails, mask_phone, mask_ip
from cs336_data.harmful_content import identify_nsfw, identify_toxic_speech
from cs336_data.gopher_quality_filters import gopher_quality_filter
from cs336_data.exact_deduplication import exact_duplicate_line
from cs336_data.minhash_deduplication import minhash_deduplication



def run_extract_text_from_html_bytes(html_bytes: bytes) -> str | None:
    return extract_text_from_html_bytes(html_bytes)


def run_identify_language(text: str) -> tuple[Any, float]:
    return identify_language(text)


def run_mask_emails(text: str) -> tuple[str, int]:
    return mask_emails(text)


def run_mask_phone_numbers(text: str) -> tuple[str, int]:
    return mask_phone(text)


def run_mask_ips(text: str) -> tuple[str, int]:
    return mask_ip(text)


def run_classify_nsfw(text: str) -> tuple[Any, float]:
   return identify_nsfw(text)


def run_classify_toxic_speech(text: str) -> tuple[Any, float]:
   return identify_toxic_speech(text)


def run_classify_quality(text: str) -> tuple[Any, float]:
    model = fasttext.load_model("/Users/huhuaxiao/Documents/GitHub/cs336-assignment4-data/data/classifiers/quality_classifier_model.bin")
    text_clean = text.replace("\n", " ").replace("\r", " ")
    prediction = model.predict(text_clean)
    labels = prediction[0][0]
    if labels[0] == "__label__positive":
        label = "wiki"
    else:
        label = "cc"
    return label, float(prediction[1][0])


def run_gopher_quality_filter(text: str) -> bool:
    return gopher_quality_filter(text)


def run_exact_line_deduplication(
    input_files: list[os.PathLike], output_directory: os.PathLike
):
    
    exact_duplicate_line(input_files, output_directory)


def run_minhash_deduplication(
    input_files: list[os.PathLike],
    num_hashes: int,
    num_bands: int,
    ngrams: int,
    jaccard_threshold: float,
    output_directory: os.PathLike,
):
    minhash_deduplication(
        input_files,
        num_hashes,
        num_bands,
        ngrams,
        jaccard_threshold,
        output_directory,)
