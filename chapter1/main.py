"""
main file for chapter1 project
it is the entry point for the project
handles the main logic of the project
"""
from report_generator import ReportGenerator



def main():
    # 1- get the template folder path
    template_folder_path = "template_config.yaml"  # also can be read from a config file or .env file
    # 2- create two report generator objects and store each in a variable
    report_generator = ReportGenerator(template_folder_path)
    # 3- call the content menu method on both objects
    report_generator.generate_content_menu(report_generator.sections)
    # add a page break
    report_generator.project_report.add_page_break()
    report_generator.prompt_eng_report.add_page_break()
    # 4- call the write the chapter method
    report_generator.write_the_chapter(report_generator.sections)
    # 5- save the document
    report_generator.save_document()
    
if __name__ == "__main__":
    main()
