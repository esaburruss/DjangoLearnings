from pages.models import Section, Page

def genNav():
    section_list = Section.objects.all()
    for x in section_list:
        x.pages = Page.objects.filter(section = x.id)
        x.length = len(x.pages)
    return section_list;

def genD(name):
    return {'sects': genNav(), 'pageName': name}

def wrap(view, pageName):
    def new_view(request, *args, **kwargs):
        d = {'sects': genNav(), 'pageName': pageName}
        return view(request, d, *args, **kwargs)
    return new_view

def wrapDash(view, pageName):
    def new_view(request, *args, **kwargs):
        d = {'sects': genNav(), 'pageName': pageName, 'edit': 'Edit'}
        return view(request, d, *args, **kwargs)
    return new_view

def delete(section, page):
    #page.delete()
    return 'deleted'

def spOrder(list):
    index = []
    for x in list:
        l = len(x)
        if 'p' in x:
            pPos = x.find('p')
            sPos = x.find('s')
            sID = int(x[sPos+1:pPos])
            pID = int(x[pPos+1:l])
            psvar = {'s': sID, 'p': pID}
            index.append(psvar)
        else:
            sID = int(x[1:l]);
            psvar = {'s': sID, 'p': -1}
            index.append(psvar)
    return index

def sectStart(index):
    arr = []
    y = 0
    for x in index:
        if(x['p'] == -1):
            arr.append(y)
        y = y + 1
    return arr

def reOrderAction(index):
    sOrder = 1
    pOrder = 1
    for i in index:
        if(i['p'] == -1):
            pOrder = 1
            section = Section.objects.get(pk = i['s'])
            section.pos = sOrder
            section.save()
            sOrder += 1
        else:
            page = Page.objects.get(pk = i['p'], section = i['s'])
            page.pos = pOrder
            page.save()
            pOrder += 1

def greekAlphabet():
	return ('Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa', 'Lambda', 'Mu', 'Nu', 'Xi', 'Omicron', 'Pi', 'Rho', 'Sigma', 'Tau', 'Upsilon', 'Phi', 'Chi', 'Psi', 'Omega')

def monthList():
    return ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC')

def pledgeClassList():
    PCs = []
    PCs.append('Charter')
    greek = greekAlphabet()
    for pc in greek:
        PCs.append(pc)
    for pc in greek:
        PCs.append('Alpha ' + pc)
    for pc in greek:
        PCs.append('Beta ' + pc)
    return PCs

def yearList(min, max):
    years = []
    while(min <= max):
        years.append(min)
        min += 1
    return years

def stateList():
    return ('AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY')
