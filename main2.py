import xlsxwriter


workbook = xlsxwriter.Workbook('data.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': True})
cell_format = workbook.add_format({'bold': True, 'font_color': 'red'})
worksheet.write('A1', 'Prop', bold)
worksheet.write('B1', 'value in DEV', bold)
worksheet.write('C1', 'value in QA', bold)
worksheet.write('D1', 'value in UAT', bold)
row = 1
col = 0
def givememap(name):
    myprops = {}
    with open(name, 'r') as f:
     for line in f:
        line = line.rstrip()
        if "=" not in line: continue
        if line.startswith("#"): continue

        k, v = line.split("=", 1)
        myprops[k] = v 
    f.close()    
    return myprops  
     
devprop=givememap("dev.prop")
qaprop=givememap("qa.prop")
uatprop=givememap("uat.prop")
super={**devprop, **qaprop, **uatprop}
print(super)

for k in super:
     worksheet.write(row, col,     k)
     if k in devprop: worksheet.write(row, col + 1, devprop[k])
     if k in qaprop: worksheet.write(row, col + 2, qaprop[k])
     if k in uatprop: worksheet.write(row, col + 3, uatprop[k])
     #if "devprop[k]" == "uatprop[k]" == "qaprop[k]":
     #if all(v == super[k] for v in [devprop[k],uatprop[k],qaprop[k]]):    
     # worksheet.set_row(row, None, cell_format)
     row += 1






workbook.close()