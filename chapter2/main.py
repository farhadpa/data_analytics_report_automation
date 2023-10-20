"""
main file for chapter2 project
it is the entry point for the project
handles the main logic of the project
"""
from report_generator import ReportGenerator


def main():
    try:
        # get the template folder path
        template_folder_path = "template_config.yaml"  # also can be read from a config file or .env file
        # create two report generator objects and store each in a variable
        report_generator = ReportGenerator(template_folder_path)
        # 3- call the content menu method 
        report_generator.generate_content_menu(report_generator.sections)
        # add a page break after content menu
        report_generator.project_report.add_page_break()
        report_generator.prompt_eng_report.add_page_break()
        # start writing chapter2
        report_generator.write_the_chapter(report_generator.sections)
        # save the document
        report_generator.save_document()
    except Exception as e:
        print(e)
        report_generator.save_document()

if __name__ == "__main__":
    main()
