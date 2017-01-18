# -*- coding: <utf-8> -*-
import xml.etree.ElementTree as ET
from shutil import copyfile

class outputParser():
    def __init__ (self, inputfile):
        self.inputfile = inputfile

        copyfile(self.inputfile, self.inputfile+"_backup")

        tree = ET.parse(self.inputfile)
        root = tree.getroot()
        #find <EqonomizeDoc version="0.5"> 

        if root.tag == 'EqonomizeDoc' and root.attrib == '{\'version\': \'0.5\'}':
            print "right Version"
        else :
            print "abort"

        self.incomeCategory = []
        self.expensesCategory = []
        self.account = []
        #list all  <category type="incomes" id="1" name="Aktien"/>
        for category in root.findall('category'):
            if category.get('type') == 'expenses':
                self.expensesCategory.append((category.get('name'),(category.get('id'))))
            if category.get('type') == 'incomes':
                self.incomeCategory.append((category.get('name'),(category.get('id'))))
        #list all  <account type="cash" id="31" name="John" initialbalance="51.00"/>
        for category in root.findall('account'):
            self.account.append((category.get('name'),(category.get('id'))))
                
    def getAccounts(self):
        return self.account

    def getExpenseCategories(self):
        return self.expensesCategory

    def getIncomeCategories(self):
        return self.incomeCategory   

    def writeLine(self, category, description, value, account, date):
        #dateformat YYYY-MM-DD

        if value[0] == '-':
            value = value[1:]
            #expenses
            #<transaction category="37" description="" from="31" type="expense" cost="13.00" date="2012-02-02"/>

            line = "<transaction category=\""
            line = line + category
            line = line + "\" description=\""
            line = line + description
            line = line + "\" from=\""
            line = line + account
            line = line + "\" type=\""
            line = line + "expense"
            line = line + "\" cost=\""
            line = line + value
            line = line + "\" date=\""
            line = line + date
            line = line + "\"/>"
        else:
            #income
            #<transaction category="21" description="" income="64.32" type="income" to="50" date="2012-02-03"/>

            line = "<transaction category=\""
            line = line + category
            line = line + "\" description=\""
            line = line + description
            line = line + "\" income=\""
            line = line + value
            line = line + "\" type=\""
            line = line + "income"
            line = line + "\" to=\""
            line = line + account
            line = line + "\" date=\""
            line = line + date
            line = line + "\"/>"
        print line
        line = line.encode('ascii', 'backslashreplace')

        with open(self.inputfile, "r") as file:
            filedata = file.read()
        filedata = filedata.replace('</EqonomizeDoc>', line + "\n </EqonomizeDoc>")
        with open(self.inputfile, 'w') as file:
            file.write(filedata)


 #<transaction category="37" description="" from="31" type="expense" cost="13.00" date="2012-02-02"/>
