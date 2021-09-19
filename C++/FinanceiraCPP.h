#ifndef FINANCEIRACPP_H
#define FINANCEIRACPP_H

double FVsimples(double PV, double i, double n);
double PVsimples(double FV, double i, double n);
double N_simples(double FV, double PV, double i);
double I_simples(double FV, double PV, double n, int digitos);

void imprimeFVsimples(double PV, double i, int n);
void imprimeFVcomposto(double PV, double i, int n);

double FVcomposto(double PV, double i, double n);
double PVcomposto(double FV, double i, double n);
double N_composto(double FV, double PV, double i);
double I_composto(double FV, double PV, double n, int digitos);

double PVparcelas(double PMT, double i, double n);
double FVparcelas(double PMT, double i, double n);
double PMT_PV_parcelas(double PV, double i, double n);
double PMT_FV_parcelas(double FV, double i, double n);

#endif
