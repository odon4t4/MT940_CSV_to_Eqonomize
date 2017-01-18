# coding=utf-8
import Tkinter as tk
from Tkinter import *
import Tkconstants, tkFileDialog
from inputParser import *
from outputParser import *
from ast import literal_eval
import datetime


class Demo1:
	def __init__(self, master):
		self.element = 0
		self.disableWrite = 0

		self.master = master
		self.frame = tk.Frame(self.master)

		#Left
		self.input = tk.Button(self.frame, text = 'Inputfile', width = 50, command = self.input).grid(row=0,column=0)

		self.dateFrame = tk.Frame(self.frame,width = 50)
		self.dateLabel = tk.Label(self.dateFrame,text="Date").grid(row=0,column=0)
		self.dateOptionList = ['DATE']
		self.dateVariable = tk.StringVar(self.master)
		self.dateVariable.set(self.dateOptionList[0])
		self.dateVariable.trace('w',self.update_outputDate)
		self.dateOptionsMenu = tk.OptionMenu(self.dateFrame,self.dateVariable, *self.dateOptionList).grid(row=0,column=1)
		self.dateFrame.grid(row=1,column=0)

		self.descriptionFrame = tk.Frame(self.frame,width = 50)
		self.descriptionLabel = tk.Label(self.descriptionFrame,text="Description").grid(row=0,column=0)
		self.descriptionOptionList = ['DESCRIPTION']
		self.descriptionVariable = tk.StringVar(self.master)
		self.descriptionVariable.set(self.descriptionOptionList[0])
		self.descriptionVariable.trace('w',self.update_outputDescription)
		self.descriptionOptionsMenu = tk.OptionMenu(self.descriptionFrame,self.descriptionVariable, *self.descriptionOptionList).grid(row=0,column=1)
		self.descriptionFrame.grid(row=2,column=0)

		self.toFrame = tk.Frame(self.frame,width = 50)
		self.toLabel = tk.Label(self.toFrame,text="To").grid(row=0,column=0)
		self.toOptionList = ['To']
		self.toVariable = tk.StringVar(self.master)
		self.toVariable.set(self.descriptionOptionList[0])
		self.toVariable.trace('w',self.update_outputTo)
		self.toOptionsMenu = tk.OptionMenu(self.toFrame,self.descriptionVariable, *self.descriptionOptionList).grid(row=0,column=1)
		self.toFrame.grid(row=3,column=0)

		self.valueFrame = tk.Frame(self.frame,width = 50)
		self.valueLabel = tk.Label(self.valueFrame,text="Value").grid(row=0,column=0)
		self.valueOptionList = ['VALUE']
		self.valueVariable = tk.StringVar(self.master)
		self.valueVariable.set(self.valueOptionList[0])
		self.valueVariable.trace('w',self.update_outputValue)
		self.valueOptionsMenu = tk.OptionMenu(self.valueFrame,self.valueVariable, *self.valueOptionList).grid(row=0,column=1)
		self.valueFrame.grid(row=4,column=0)

		self.accFrame = tk.Frame(self.frame,width = 50)
		self.accLabel = tk.Label(self.accFrame,text="Account").grid(row=0,column=0)
		self.accFrame.grid(row=5,column=0)

		self.catFrame = tk.Frame(self.frame,width = 50)
		self.catLabel = tk.Label(self.catFrame,text="Category").grid(row=0,column=0)
		self.catFrame.grid(row=6,column=0)


		#Right
		self.output = tk.Button(self.frame, text = 'Outputfile', width = 50, command = self.output).grid(row=0,column=1)

		self.outputDateVariable			= tk.StringVar(self.master)
		self.outputDescriptionVariable 	= tk.StringVar(self.master)
		self.outputToVariable 			= tk.StringVar(self.master)
		self.outputValueVariable 		= tk.StringVar(self.master)

		self.outputDate 		= Entry(self.frame,textvariable=self.outputDateVariable,width = 50)
		self.outputDate.grid(row=1,column=1)
		self.outputDescription 	= Entry(self.frame,textvariable=self.outputDescriptionVariable,width = 50)
		self.outputDescription.grid(row=2,column=1)

		#self.outputto			= Entry(self.frame,textvariable=self.outputToVariable,width = 50)
		self.outputto			= Label(self.frame,textvariable=self.outputToVariable,width = 50)
		self.outputto.grid(row=3,column=1)

		self.outputValue 		= Entry(self.frame,textvariable=self.outputValueVariable,width = 50)
		self.outputValue.grid(row=4,column=1)

		self.outputAccOptionList = ['Account']
		self.outputAccVariable = tk.StringVar(self.master)
		self.outputAccVariable.set(self.outputAccOptionList[0])
		self.outputAccOptionsMenu = tk.OptionMenu(self.frame,self.outputAccVariable, *self.outputAccOptionList).grid(row=5,column=1)

		self.outputCatOptionList = ['Category']
		self.outputCatVariable = tk.StringVar(self.master)
		self.outputCatVariable.set(self.outputCatOptionList[0])
		self.outputCatOptionsMenu = tk.OptionMenu(self.frame,self.outputCatVariable, *self.outputCatOptionList).grid(row=6,column=1)

		#next
		self.nextButton = tk.Button(self.frame, text = 'next', width = 50, command = self.next)
		self.nextButton.grid(row=7,column=0)

		#write and next
		self.writeButton = tk.Button(self.frame, text = 'write "and next"', width = 50, command = self.write)
		self.writeButton.grid(row=7,column=1)

		self.frame.pack()

	def input(self):
		self.inputFilename = tkFileDialog.askopenfilename(initialdir = ".",title = "Select Inputfile",filetypes = (("CSV files","*.CSV"),("all files","*.*")))
		self.parser = inputParser(self.inputFilename)

		self.update_dateDropDown()
		self.update_toDropDown()
		self.update_valueDropDown()
		self.update_descriptionDropDown()


	def output(self):
		self.outputFilename = tkFileDialog.askopenfilename(initialdir = ".",title = "Select Outputfile",filetypes = (("realy all files","*"),("all files","*.*")))
		self.outputParser = outputParser(self.outputFilename)

		self.update_outputAccount()
		self.update_outputCattegory()

	def write(self):
		self.outputParser = outputParser(self.outputFilename)
		category 	= literal_eval(self.outputCatVariable.get())[1]
		description	= self.outputDescriptionVariable.get()
		value		= self.outputValueVariable.get()
		account		= literal_eval(self.outputAccVariable.get())[1]
		date		= self.outputDateVariable.get()

		self.outputParser.writeLine(category,description,value,account,date)

		self.next()

	def next(self):
		self.element = self.element + 1

		if self.disableWrite == 1:
			self.writeButton.config(state='disabled')

		if self.parser.isElemetLeft(self.element) == 0:
			self.nextButton.config(state='disabled')
			self.disableWrite = 1


		self.update_outputValue()
		self.update_outputTo()
		self.update_outputDescription()
		self.update_outputDate()

	def update_outputAccount(self):
		self.outputAccOptionList = self.outputParser.getAccounts()
		self.outputAccVariable.set(self.outputAccOptionList[0])
		self.outputAccOptionsMenu = tk.OptionMenu(self.frame,self.outputAccVariable, *self.outputAccOptionList).grid(row=4,column=1)


	def update_outputCattegory(self):	
		self.outputCatOptionList = self.outputParser.getExpenseCategories()
		self.outputCatVariable.set(self.outputCatOptionList[0])
		self.outputCatOptionsMenu = tk.OptionMenu(self.frame,self.outputCatVariable, *self.outputCatOptionList).grid(row=5,column=1)

	def update_dateDropDown(self):
		self.dateOptionList = self.parser.getKeys()
		self.dateVariable.set(self.dateOptionList[2])
		self.dateOptionsMenu = tk.OptionMenu(self.dateFrame,self.dateVariable, *self.dateOptionList).grid(row=0,column=1)

	def update_descriptionDropDown(self):
		self.descriptionOptionList = self.parser.getKeys()
		self.descriptionVariable.set(self.descriptionOptionList[4])
		self.descriptionOptionsMenu = tk.OptionMenu(self.descriptionFrame,self.descriptionVariable, *self.descriptionOptionList).grid(row=0,column=1)

	def update_toDropDown(self):
		self.toOptionList = self.parser.getKeys()
		self.toVariable.set(self.toOptionList[5])
		self.toOptionsMenu = tk.OptionMenu(self.toFrame,self.toVariable, *self.toOptionList).grid(row=0,column=1)


	def update_valueDropDown(self):
		self.valueOptionList = self.parser.getKeys()
		self.valueVariable.set(self.valueOptionList[8])
		self.valueOptionsMenu = tk.OptionMenu(self.valueFrame,self.valueVariable, *self.valueOptionList).grid(row=0,column=1)

	def update_outputDate(self,*args):
		date = self.parser.getValue(self.element, self.dateVariable.get())
		d=datetime.datetime.strptime(date,'%d.%m.%y')
		self.outputDateVariable.set(d.strftime('%Y-%m-%d'))

	def update_outputValue(self,*args):
		self.outputValueVariable.set(self.parser.getValue(self.element, self.valueVariable.get()))

	def update_outputDescription(self,*args):
		self.outputDescriptionVariable.set(
			self.suggestions(
				self.parser.getValue(
					self.element, self.descriptionVariable.get()),
				self.parser.getValue(
					self.element, self.toVariable.get())))

	def update_outputTo(self,*args):
		self.outputToVariable.set(self.parser.getValue(self.element, self.toVariable.get()))

	def suggestions(self,description,to):
		listOfSearchElementsTo 	= 	[("","Substitution"),
									("","Substitution")]
									
		listOfSearchElementsDesc =	[("","Substitution"),
									("","Substitution")]
		
		for x in listOfSearchElementsTo:
			if x[0] in to:
				return x[1]
		for y in listOfSearchElementsDesc:
			if y[0] in description:
				return y[1]
		return description


def main(): 
	root = tk.Tk()
	app = Demo1(root)
	root.mainloop()

if __name__ == '__main__':
	main()


