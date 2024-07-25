import json
import argparse

def process_entry(entry, entry_type):
    sentence, subject, attribute = entry
    # Truncate the sentence at the attribute word
    truncated_sentence = sentence.split(attribute)[0].strip()
    # Replace the subject with {} in the truncated sentence
    truncated_sentence = truncated_sentence.replace(subject, '{}')
    # Create the new format
    return {
        "prompt": truncated_sentence + " ",
        "subject": subject,
        "target_new": {
            "str": attribute
        },
        "type": entry_type
    }

def process_file(input_filename, output_filename, entry_type):
    with open(input_filename, 'r') as infile:
        data = json.load(infile)
    
    processed_data = [process_entry(entry, entry_type) for entry in data]
    
    with open(output_filename, 'w') as outfile:
        json.dump(processed_data, outfile, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Process JSON files for GPT model training.")
    parser.add_argument('input_file', type=str, help='The input JSON file to be processed.')
    parser.add_argument('output_file', type=str, help='The output JSON file after processing.')
    parser.add_argument('type', type=str, help='The type for the processed entries.')

    args = parser.parse_args()

    process_file(args.input_file, args.output_file, args.type)

if __name__ == "__main__":
    main()