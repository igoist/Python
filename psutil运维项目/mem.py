#-*-coding:utf-8-*-

import psutil as ps

# 读取并返回总内存占用量
def mem():
    dic = {}
    phymem = ps.virtual_memory()
    dic['v_used'] = phymem.used
    dic['v_total'] = phymem.total
    dic['v_percent'] = str(phymem.percent)
    phymem = ps.swap_memory()
    dic['s_used'] = phymem.used
    dic['s_total'] = phymem.total
    dic['s_percent'] = str(phymem.percent)
    return dic

# 根据 mem() 返回内容打印格式字符串
def memory_print(unit='G'):
    # phymem = ps.virtual_memory()
    dic = mem()
    # line = "内存 memory: %s / %s 相当于 %5s%% "
    # if (unit == "G") or (unit == "g"):
    #     line = line %(
    #             str(float(dic["used"]/1024.0/1024.0/1024))+"G",
    #             str(float(dic["total"]/1024.0/1024.0/1024))+"G",
    #             dic["percent"],
    #             )
    # else:
    #     line = line %(
    #             str(float(dic["used"]/1024.0/1024.0))+"M",
    #             str(float(dic["total"]/1024.0/1024.0))+"M",
    #             dic["percent"],
    #             )
    line = ''
    p_pt = '1'
    p_fc = '32'
    p_bc = '40'
    p_tag = print_tag(p_pt, p_fc, p_bc)
    pe_flag = '\033[0m' # means: style print end flag
    if (unit == "G") or (unit == "g"):
        line = '虚拟内存 virtual memory: ' + p_tag + ' ' + str(float(dic['v_used']/1024.0/1024.0/1024)) + 'G / ' + str(float(dic['v_total']/1024.0/1024.0/1024)) + 'G' + ' - ' + dic['v_percent'] + '%' + ' ' + pe_flag + '\n'
        line += '交换内存    swap memory: ' + p_tag + ' ' + str(float(dic['s_used']/1024.0/1024.0/1024)) + 'G / ' + str(float(dic['s_total']/1024.0/1024.0/1024)) + 'G' + ' - ' + dic['s_percent'] + '%' + ' ' + pe_flag
    else:
        line = '虚拟内存 virtual memory: ' + p_tag + ' ' + str(float(dic['v_used']/1024.0/1024.0)) + 'M / ' + str(float(dic['v_total']/1024.0/1024.0)) + 'M' + ' - ' + dic['v_percent'] + '%' + ' ' + pe_flag + '\n'
        line += '交换内存    swap memory: ' + p_tag + ' ' + str(float(dic['s_used']/1024.0/1024.0)) + 'M / ' + str(float(dic['s_total']/1024.0/1024.0)) + 'M' + ' - ' + dic['s_percent'] + '%' + ' ' + pe_flag
    print line
    return line


# start the main func
# memory_print()

# toggle font color in shell
def print_tag(p_pattern, p_front_color, p_back_color):
    return '\033[' + p_pattern + ';' + p_front_color + ';' + p_back_color + 'm'

