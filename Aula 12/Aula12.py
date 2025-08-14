# sistema de calculo de salário 


# parâmeto


def valor_hora(carga, salario):
    calculo = salario/carga
    return calculo


def hora_extra(v_hora):
    return v_hora * 1.5


def quantidade_extra(q,hora_extra):
    cal = q * hora_extra
    return cal



def salario_total(extra,salario):
    c = extra + salario
    return c


def sistema_rh():
    print('SISTEMA RH')
    print('Valor Hora')
    carga_func = float(input('Carga horária: '))
    salario1 = float(input('Salário: '))
    valor_h = valor_hora(carga_func,salario1)
    print('Valor hora R$', round(valor_h,2))
    print('***' * 15)
    print('Hora Extra:')
    extra_h  = hora_extra(valor_h)
    print('Valor extra R$',round(extra_h))
    print('***' * 15)
    print('Quantidade de hora e valor a pagar')
    qua = float(input('Quantidade de horas'))
    quantidade_e_  = quantidade_extra(qua,extra_h)
    print('hora extra', qua ,'R$', round(quantidade_e_,2))
    print('***' * 15)
    print('Total a pagar')
    total =  salario_total(quantidade_e_,salario1)
    print('R$', round(total,2))


sistema_rh()