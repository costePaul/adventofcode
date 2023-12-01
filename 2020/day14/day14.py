def turn_to_b(val):
    out = ''
    val = int(val)
    while val>0:
        if val%2:
            _out = '1'
        else:
            _out = '0'
        out = _out+out
        val = val//2
    n = 36-len(out)
    return '0'*n+out

def turn_b_to_n(bin):
    out = 0
    total_len = len(bin)
    for i,char in enumerate(bin):
        out += int(char) * 2**(total_len-1-i)
    return out

def read_mask(input):
    # mask = X11001110001101XX01111X1001X01101111
    mask = input.strip().split('=')[1].strip()
    return mask

def read_mem_assign_1(input):
    # mem[32163] = 23587
    a,b = input.strip().split('=')
    idx = a.strip().split('[')[1].strip()[:-1]
    val = b.strip()
    return idx, turn_to_b(val)

def read_mem_assign_2(input):
    # mem[32163] = 23587
    a,b = input.strip().split('=')
    idx = a.strip().split('[')[1].strip()[:-1]
    val = b.strip()
    return turn_to_b(idx), val

def apply_mask_1(mask,val):
    out = ''
    for a,b in zip(mask,val):
        if a == 'X':
            out+=b
        else:
            assert(a in '01')
            out+=a
    return out

def generate_idx(bit):
    for i,char in enumerate(bit):
        if char == 'X':
            bit_wz = bit[:i]+'1'+bit[i+1:]
            bit_wo = bit[:i]+'0'+bit[i+1:]
            return generate_idx(bit_wz) + generate_idx(bit_wo)
    return [bit]

def apply_mask_2(mask,val):
    out = ''
    for a,b in zip(mask,val):
        if a == '0':
            out+=b
        elif a== '1':
            out+='1'
        else:
            out+='X'
    return generate_idx(out)

def compute1(mem, instrus):
    if instrus != []:
        mask = read_mask(instrus[0])
    for instru in instrus[1:]:
        idx,val = read_mem_assign_1(instru)
        mem[idx] = apply_mask_1(mask, val)
    return mem

def compute2(mem, instrus):
    if instrus != []:
        mask = read_mask(instrus[0])
    for instru in instrus[1:]:
        idx,val = read_mem_assign_2(instru)
        for _idx in apply_mask_2(mask, idx):
            mem[_idx] = val
    return mem

def sum_mem(mem, part_number):
    out = 0
    for key in mem.keys():
        if part_number == 1:
            out+= turn_b_to_n(mem[key])
        elif part_number == 2:
            out+= int(mem[key])
    return out

def main(part_number):
    compute = [compute1,compute2][part_number-1]
    with open('./2020/day14/input.txt', "r") as f:
        instructions = f.read().split("\n")
    n = len(instructions)
    i=0
    local_instru = []
    mem = {}
    while i<n:
        new_instru = instructions[i]
        if new_instru[:4]=="mask":            
            mem = compute(mem,local_instru)
            local_instru = [new_instru]
        else:
            local_instru.append(new_instru)
        i+=1
    mem = compute(mem,local_instru)
    print(sum_mem(mem, part_number))

if __name__ == '__main__':
    # main(1)
    main(2)
