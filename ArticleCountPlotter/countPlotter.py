import re
import pandas as pd
import matplotlib.pyplot as plt

def sort_by_second_value(input_dict):
    sorted_dict = dict(sorted(input_dict.items(), key=lambda x: x[1],reverse=True))
    return sorted_dict


def convert_to_csv(file):

    excel_file = file
    df = pd.read_excel(excel_file)
    csv_string = df.to_csv(index=False)
    return csv_string


def count_ids(csv_string):
    id_pattern = r'\((\d+)\)'
    
    matches = re.findall(id_pattern, csv_string)
    
    id_count = {}
    for match in matches:
        id_count[match] = id_count.get(match, 0) + 1
    
    return id_count


def plot_bar_chart(data):
    ids = list(data.keys())
    counts = list(data.values())

    plt.figure(figsize=(10, 6))
    plt.bar(ids, counts, color='skyblue')
    plt.xlabel('ID')
    plt.ylabel('Count')
    plt.title('Count of IDs')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()
    plt.show()


def get_name_by_id(csv_data, target_id):
    # Regular expression to match the pattern "Name (ID)"
    pattern = r'([\w\s-]+)\s\(({})\)'.format(re.escape(target_id))

    # Search for the pattern in the CSV data
    match = re.search(pattern, csv_data)

    # If the pattern is found, return the name, otherwise return None
    if match:
        return match.group(1)
    else:
        return None



xlsx_dir = './input.xlsx'
csv = convert_to_csv(xlsx_dir)
resault = count_ids(csv)
sort_resault = sort_by_second_value(resault)
top_10 = dict(list(sort_resault.items())[:10])

modified_data = {}
for key,value in top_10.items():
    name = get_name_by_id(csv,str(key))
    mod_key = str(name)+'\n' + str(key)
    modified_data[mod_key]=value
print(modified_data)
    
plot_bar_chart(modified_data)

