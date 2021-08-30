import argparse
import csv
import json


# argparse 설정
parser = argparse.ArgumentParser()
parser.add_argument("name", type=str, help="파일 이름")
parser.add_argument("-t", "--title", action="store_true", help="제목도 저장할지 여부")
parser.add_argument("-c", "--contents", action="store_true", help="본문도 저장할지 여부")

args = parser.parse_args()

# 파일 이름
file_name = args.name
if file_name.endswith(".json"):
    file_name = file_name[:-5]

# 파일 열기
csv_file = open(f"{file_name}.csv", "w", encoding="utf-8", newline="")
writer = csv.writer(csv_file)
writer.writerow(["content", "labels"])

json_file = open(f"{file_name}.json", "r", encoding="utf-8")
data = json.load(json_file)["data"]

# 기록
for d in data:
    if args.title:
        writer.writerow([d["title"], 0])

    if args.contents:
        key = "contents" if "contents" in d else "content"
        if d[key]:
            content = d[key].replace("\n", " ")
            writer.writerow([content, 0])

    for comments in d["comments"]:
        writer.writerow([comments, 0])

json_file.close()
csv_file.close()
