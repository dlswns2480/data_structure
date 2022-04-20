from circularDoublyLinkedList import *


def do_sim(cache_slots):

    cache_hit = 0
    tot_cnt = 0
    
    data_file = open("linkbench_short.trc")
    
    cache_item = CircularDoublyLinkedList()

    for line in data_file.readlines():
        lpn = line.split()[0]
        if lpn not in cache_item: 
            if cache_item.size() < cache_slots:
                cache_item.append(lpn)
                tot_cnt += 1
            else :
                cache_item.pop(0)
                cache_item.append(lpn)
                tot_cnt += 1
        else :
            cache_item.remove(lpn)
            cache_item.append(lpn)
            cache_hit +=1
            tot_cnt += 1
        
        

        # do programming here! 

    print("cache_slot = ", cache_slots, "cache_hit = ", cache_hit, "hit ratio = ", cache_hit / tot_cnt)

if __name__ == "__main__":

    for cache_slots in range(100, 1000, 100):
        do_sim(cache_slots)
