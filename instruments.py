from subprocess import *
""" Модуль содержит все об инструментах"""

def run_owasp_zap(domain):
    try:
        run([f"/Applications/OWASP\ ZAP.app/Contents/Java/zap.sh -cmd -quickurl {domain} -quickout ~/Documents/scan_reports/owasp_zap_report.xml -quickprogress"], shell=True, check=True)
    except (CalledProcessError):
        print("Scanner OWASP ZAP finished with non zero code")

