from enchant.checker import SpellChecker
import glob


def is_encrypted(file_content, file_name):
	row_num = 0
	encrypted = False
	d = SpellChecker("en_US")
	for rows in file_content:
		row = rows.split()
		errors_in_row = 0
		row_num += 1
		for x in row:
			d.set_text(x)
			errors = [err.word for err in d]
			if errors:
				errors_in_row += 1
			if len(errors) > 1 or errors_in_row > 2:
				print(f"The content of file {file_name} in row {row_num} may be encrypted!")
				encrypted = True
				break
	if not encrypted:
		print(f"The file '{file_name[2:]}' is not encrypted!")


def main():
	all_files = glob.glob('test_folder/*.txt')
	print(f"----------------------------------------------------- \n"
		  f"[*] Checking the following files: \n {all_files}")
	for file in all_files:
		file_content = open(file, "r")    # read only
		is_encrypted(file_content, str(file))


if __name__ == "__main__":
	main()


