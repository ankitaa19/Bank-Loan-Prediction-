from backend.preprocessing import LoanPreprocessor

pre = LoanPreprocessor()

print("Education values:")
print(pre.dataset_info()["Education"].unique())

print("\nEducation Mapping:")
print(pre.show_mapping("Education"))
