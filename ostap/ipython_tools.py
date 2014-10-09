import ROOT
from IPython.display import HTML


def params_table(fit_result):
    """Returns RooFitResult as HTML for IPython notebook"""
    if not type(fit_result) == ROOT.RooFitResult:
        raise Exception('fit_result is not an instance of ROOT.RooFitResult')

    statuses = {
        -1 : "Unknown, matrix was externally provided",
        0  : "Not calculated at all",
        1  : "Approximation only, not accurate",
        2  : "Full matrix, but forced positive-definite",
        3  : "Full, accurate covariance matrix"
    } # see http://root.cern.ch/root/html/src/RooFitResult.cxx.html

    s  = "Fit status: <b>{}</b><br/>".format(statuses[fit_result.covQual()])
    s += "minNll: <b>{}</b><br/>".format(fit_result.minNll())
    s += "<table><tr><th>Name</th> <th>Value</th> <th>Min</th> <th>Max</th> </tr>"

    eps = 1e-10
    for name, val in fit_result.parameters().items():
        d_low  = (val[0].value() - val[1].getMin(), val[1].getMin())
        d_high = (val[0].value() - val[1].getMax(), val[1].getMax())

        delta, norm = min(d_low, d_high, key=lambda x: x[0])
        
        if abs(norm) < eps:
            norm = eps
        
        if abs(float(delta) / norm) < 1e-3:
            s += '<tr><th><font color="red">{}</font></th> <th>{}</th> <th>{}</th> <th>{}</th></tr>'.format(name, val[0], val[1].getMin(), val[1].getMax())
        else:
            s += '<tr><th>{}</th> <th>{}</th> <th>{}</th> <th>{}</th></tr>'.format(name, val[0], val[1].getMin(), val[1].getMax())

    s += "</table>"
    html = HTML(s); 

    return html
