import pdf_reader
import os
import argparse
import page_classification
import ocr_extraction
import key_value_extraction
import table_extraction
import post_processing

def check_page(data):
    result = {}
    for key, value in data.items():
        if isinstance(value, dict) and value:
            result[key] = list(value.keys())
        else:
            result[key] = []
    
    return result



if __name__ == '__main__':
    # set of arguments
    parser = argparse.ArgumentParser(description='Convert a PDF file to images')
    parser.add_argument('pdf_path', type=str, help='Path to the PDF file')

    args = parser.parse_args()
    pdf_path = args.pdf_path
    base_dir = os.path.splitext(pdf_path)[0]
    pdf_reader.convert_to_images(pdf_path)
    ocr_path = os.path.join(base_dir, "ocr_results.json")
    ocr_extraction.extract_text_from_images(base_dir)
    classified_results = page_classification.classify_images(base_dir)
    classification_keys = check_page(classified_results)
    
    key_value_results = key_value_extraction.extract_key_info_from_ocr_results(
        ocr_path,classification_keys
        )
    
    table_results = table_extraction.extract_tables_from_images(base_dir)

    post_processing.extract_combined_information(
        classified_results, key_value_results, table_results, base_dir
    )
    




