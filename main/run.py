#coding=utf-8
import os
import threading
import pytest
from common.report import Report

project_root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
report_dir = os.path.join(project_root, 'report')
result_dir = os.path.join(report_dir, 'allure_result')
print(result_dir)
allure_report = os.path.join(report_dir, 'allure_report')
report = Report()

def run_pytest():
    pytest.main(['-v', '-s', f'--alluredir={result_dir}'])


def general_report():
    cmd = "{} generate {} -o {} --clean".format(report.allure, result_dir, allure_report)
    print("ddd")
    print(os.popen(cmd).read())
    print("ccc")


if __name__ == '__main__':
    run = threading.Thread(target=run_pytest)
    gen = threading.Thread(target=general_report)
    run.start()
    run.join()
    gen.start()