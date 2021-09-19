#include<iostream>
#include<cmath>
using namespace std;

double FVsimples ( double PV, double i, double n )
{
	return PV * (1 + i * n);
}

double PVsimples(double FV, double i, double n)
{
	return FV / (1 + i*n);
}

double N_simples(double FV, double PV, double i)
{
	return ((FV / PV) - 1) / i;
}

double I_simples(double FV, double PV, double n, int digitos)
{
	return ((FV / PV) - 1) / n;
}

double FVcomposto(double PV, double i, double n)
{
	return PV * (pow((1 + i), n));
}

double PVcomposto(double FV, double i, double n)
{
	return FV * (1 / (  pow((1 + i), n)));
}

double N_composto(double FV, double PV, double i)
{
	return log10(FV / PV) / log10(1 + i);
}

double I_composto(double FV, double PV, double n, int digitos)
{
	return	pow((FV / PV), (1 / n)) - 1;
}

void imprimeFVsimples(double PV, double i, int n)
{
	double parc = PV * i;
	double aux = PV + parc;
	cout << "-----" << endl;
	cout << "Valores por periodo: (Opcao: Juros Simples)" << endl;
	cout << "---" << endl;
	cout << "Valor Inicial: $" << PV << endl;
	for (int idx = 1; idx <= n; idx++){
		cout << "Periodo " << idx << ": $" << aux << endl;
		aux += parc;
	}
	cout << "-----" << endl;
}

void imprimeFVcomposto(double PV, double i, int n)
{
	double juros = (1+i);
	double aux = PV * juros;
	cout << "-----" << endl;
	cout << "Valores por periodo: (Opcao: Juros Compostos)" << endl;
	cout << "---" << endl;
	cout << "Valor Inicial: $" << PV << endl;
	for (int idx = 1; idx <= n; idx++) {
		cout << "Periodo " << idx << ": $" << aux << endl;
		aux *= juros;
	}
	cout << "-----" << endl;
}




double PVparcelas(double PMT, double i, double n)
{
	double aux = pow( (1 + i), n);
	return PMT * ((aux - 1) / (i * aux));
}
double FVparcelas(double PMT, double i, double n)
{
	double aux = pow( (1 + i), n);
	return PMT * ((pow((1 + i), n) - 1) / i);
}

double PMT_PV_parcelas(double PV, double i, double n)
{
	double aux = pow((1 + i), n);
	return PV * ((i * aux) / (aux - 1));
}

double PMT_FV_parcelas(double FV, double i, double n)
{
	return FV * (i / (pow((1 + i), n) - 1));
}
