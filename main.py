import csv
import json

from function import *


class DomainFinder:

    def __init__(self):
        self.fields = [
            "domain_name", "registrar", "whois_server", "referral_url", "updated_date", "creation_date",
            "expiration_date", "name_servers", "status", "emails", "dnssec", "name", "org", "address", "city", "state",
            "registrant_postal_code", "country",
        ]
        self.filename = "Data set.csv"
        self.lines = []
        with open(self.filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.fields)
        file_path = input("Enter the file Relative path : ")
        if file_path:
            self.read_file(file_path)

    def read_file(self, file_path):
        with open(file_path) as f:
            self.lines = [line.rstrip() for line in f]
        self.domain_finder()

    def domain_finder(self):
        for companyName in self.lines:
            url = getURL(companyName)
            if url:
                domain_info = domain_info_fun(url)
                if domain_info:
                    data = dict_update(domain_info)
                    print(json.dumps(data, indent=2))
                    with open(self.filename, 'a') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=self.fields, delimiter="|")
                        writer.writerow(data)


DomainFinder()
