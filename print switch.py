import tkinter as tk
import subprocess


class PrinterManager(tk.Frame):

    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.configure_interface()
        self.create_widgets()

    def configure_interface(self):
        self.master.title('Printer Manager')
        self.master.geometry('300x100')
        self.master.resizable(False, False)
        self.master.config(background='#626a77')

    def create_widgets(self):
        self.default_printer_label = tk.Label(self.master, bg='#626a77', fg='white')
        self.default_printer_label.place(x=10, y=12)

        printer_RICOH = tk.Button(self.master, text='RICOH Aficio MP 3352', command=lambda: self.set_RICOH())
        printer_RICOH.place(x=12, y=65)

        printer_OTHER = tk.Button(self.master, text='HP LasetJet P1102', command=lambda: self.set_HP())
        printer_OTHER.place(x=12, y=35)

    def set_RICOH(self):
        subprocess.call("wmic printer where name='{:}' call setdefaultprinter".format('RICOH Aficio MP 3352'),
                        stdin=None,
                        stdout=None, stderr=None, shell=True)
        subprocess.call("msg /time:10 * {:} ".format('"Default: RICOH Aficio MP 3352"'), stdin=None, stdout=None,
                        stderr=None,
                        shell=True)
        self.status(True, False)

    def set_HP(self):
        subprocess.call("wmic printer where name='{:}' call setdefaultprinter".format('HP LasetJet P1102'), stdin=None,
                        stdout=None, stderr=None, shell=True)
        subprocess.call("msg /time:10 * {:} ".format('"Default: LasetJet P1102"'), stdin=None, stdout=None,
                        stderr=None,
                        shell=True)
        self.status(False, True)

    def status(self, RICOH=False, HP=False):
        if RICOH:
            ok_printer_label = tk.Label(self.master, bg='#626a77', fg='white')
            ok_printer_label.config(text="✔")
            ok_printer_label.place(x=150, y=65)

        if HP:
            ok_printer_label = tk.Label(self.master, bg='#626a77', fg='white')
            ok_printer_label.config(text="✔")
            ok_printer_label.place(x=150, y=35)


if __name__ == '__main__':
    root = tk.Tk()
    PrinterManager(root)
    root.mainloop()
