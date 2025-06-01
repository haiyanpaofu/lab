from Bio import SeqIO
import os

def calculate_gc_content(sequence):
    """计算序列的CG数量"""
    sequence = sequence.upper()
    gc_count = sequence.count('G') + sequence.count('C')
    return gc_count / len(sequence)

def process_genbank_file(filename):
    """
    核心代码-读取genbank文件计算每个序列的CG含量并按升序输出结果
    """
    sequences_with_gc = []
    for record in SeqIO.parse(filename, "genbank"):
        gc_content = calculate_gc_content(record.seq)
        sequences_with_gc.append((record.id, record.description, gc_content, str(record.seq)))

    # 按CG数量对序列进行排序升序
    sorted_sequences = sorted(sequences_with_gc, key=lambda x: x[2])