<template>
    <!-- <h1>方向介绍</h1> -->
    <div class="tz-gallery">
					
                    <b>方向介绍：</b>		
                    
                    <p style="font-size:0.9rem;">
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;高性能计算（High performance computing）指通常使用很多处理器（作为单个机器的一部分）或者某一集群中组织的几台计算机（作为单个计算资源操作）的计算系统和环境。高性能集群上运行的应用程序一般使用并行算法，把一个大的普通问题根据一定的规则分为许多小的子问题，在集群内的不同节点上进行计算，而这些小问题的处理结果，经过处理可合并为原问题的最终结果。由于这些小问题的计算一般是可以并行完成的，从而可以缩短问题的处理时间。
                                    <br>
                                    <br>
                                    
                                    </p><div align="center">
                                        <a class="lightbox">
                                            <img class="research-sm-img" height="400" width="400" src="../../assets/researchIntro/chatu_gxn.jpg" alt="Coast">
                                        </a>
                                    </div>
                                    
                                    &nbsp;&nbsp;&nbsp;&nbsp;高性能集群在计算过程中，各节点是协同工作的，它们分别处理大问题的一部分，并在处理中根据需要进行数据交换，各节点的处理结果都是最终结果的一部分。高性能集群的处理能力与集群的规模成正比，是集群内各节点处理能力之和，但这种集群一般没有高可用性。高性能计算的分类方法很多。这里从并行任务间的关系角度来对高性能计算分类。
                                    <br>
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;高吞吐计算（High-throughput Computing）是高性能计算的类别之一，可以把它分成若干可以并行的子任务，而且各个子任务彼此间没有什么关联。因为这种类型应用的一个共同特征是在海量数据上搜索某些特定模式，所以把这类计算称为高吞吐计算。所谓的Internet计算都属于这一类。按照Flynn的分类，高吞吐计算属于SIMD （Single Instruction Multiple Data ，单指令多数据流）的范畴。
                                    <br>
                                    <br>
                                    分布计算（Distributed Computing）刚好和高吞吐计算相反，它们虽然可以分成若干并行的子任务，但是子任务间联系紧密，需要大量的数据交换。按照Flynn的分类，分布式的高性能计算属于MIMD（Multiple Instruction Multiple Data，多指令流-多数据流）的范畴。
                                    <br>
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;高性能计算机典型的应用领域有：
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;1. 气象预报：借助超级计算机能够模拟复杂的气流、洋流变化，能够预测天气走向。
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;2. 计算化学应用：传统的计算化学主要是研究原子和分子尺度的小分子体系的行为和相互作用。在这个领域里使用的计算理论主要包括Hartree-Fock方法（HF）、密度泛函理论（DFT）、多体扰动理论（MBPT）、组态相互作用理论（CI）和藕合簇理论（CC）等。高性能计算机能很好解决这些计算的准确性。
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;3. 发现生命秘密：从基因学的数据密集型研究到细胞网络模拟，超级计算机将帮助寻找生命的秘密。
                                    <br>
                                    &nbsp;&nbsp;&nbsp;&nbsp;4. 流体力学、地质模拟等大型科学计算领域、以及人工智能的一些领域。
                    
                    <p></p>
                    
                                    </div>
</template>