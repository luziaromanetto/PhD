# PhD

## TODO list:
> - read the rossi new paper, to understand the cost function in the other paper;
> - talk with Alneu about the project;
> - read in details the famous paper "Learning with local and global consistence";
> - read Rossi Theses
> - read Thiago Theses

## Think about:
> - In tersor decomposition we focous on objects representation but not much in the relation of the objects like in the field of heterogeneous network, but the concept of schema network is very close to network graphs, for me this to adeas can be combineted to generete new decomposition or solve some problems of one field with thecniques of the other, or to generate syntetic data tensor.

### week 18/09 to 21/09
> - working on the course project.
> - Finishing the DBLP pre-processing

### week 11/09 to 15/09
> - read "HetPathMine: A Novel Transductive Classification Algorithm on Heterogeneous Information Networks" to the project
> - read "Graph Regularized Meta-path Based Transductive Regression in Heterogeneous Information Network"
> > - Good paper, but is about regression no classification
> - work to process curent DBLP dataset
> > - It was hard

### week 04/09 to 08/09
> - working on the course project.
> - read "A Survey of Heterogeneous Information Network Analysis"

### week 28/08 to 01/09
> - reading "A Survey of Heterogeneous Information Network Analysis"
> - working in tests of BPG with faces images;
> > - It works for digits database, but not in the chineses faces yet;
> - writing the new project;
> - lecture about readed paper;
> - studing about statistics;
> - read "Graph Regularized Transductive Classification on Heterogeneous Information Networks", for lecture;


### week 21/08 to 25/08
> - writing the new project;
> - reading "Graph Regularized Transductive Classification on Heterogeneous Information Networks", for lecture.
> - Finish code for BG;
> > Good results
> > Thinking in comper with LDA
> - read the unpublished paper;
  
### week 14/08 to 18/08

> - trying to install linux on my new computer;
> > This has taken me too much time.
> - reading the unpublished paper;
> - testing PBG implementation to use that in images;
> > Testing... It looks like it's working, will comper with NMF clustering with kmeans and HLC.
> > Need to finish to read the unpublished paper to understand the implementation, but I already undertood have give the imput graph.
> - read the paper *Optimizing the class information divergence for transductive classification of texts using propagation in bipartite graphs*
> > Interesting paper has a transductive method to classify documents and terms, base on a subset of labeled documents.
> > **Note**
> > - I didn't understand the need for de Cji, the paper say that it is for terms that has many meaning in a same document, but I didn't understand this.


### week 07/08 to 11/08
> - reading the paper *Optimizing the class information divergence for transductive classification of texts using propagation in bipartite graphs*
> - look for a image dataset to test the Alneu idea of thest the PBG in this context.
> > Dwnloading th datasts available in: http://www.face-rec.org/databases/
> - read the paper *Optimization and label propagation in bipartite heterogeneous networks to improve transductive classification of texts*
> > This paper propose the transductive method named TCBHN, that is based on the minimization of a objective function that is builded over the assumtion *that the information of documents in Dl and Du are useful to induce the class information of th terms, and the induced class information for the terms aids the improvement of the class information of documents in Du*.
> > This paper is really intersting because they run a large amont of tests and comper many transductive methods, thy show that the proposed method is better or equivalent to state of art methods. **They perform statisticals methods to ensure the results**, that is a good pratice.
> >
> > **Notes :** 
> > - I don't understand way the cost function have the exponent 2 outside of the summantion, I think that his may cause an error cancellation and no the optimal result.
> - read about and organize the benchmarking text collections ( see the paper from Rossi )
> > I did collect the text datasets available in http://sites.labic.icmc.usp.br/ragero/jipm_2015/
> - read the paper *A Parameter-Free Label Propagation Algorithm Using Bipartite Heterogeneous Networks for Text Classification*
> > In this paper is propose a transductive method that model documents and terms as a bipartite graph, and build a matrix of weights from that. With the weight matrix, they build a new stochastic matrix, with this matrix and some labeled documents the run a fixed-point method to propagate the label and estimate the label of unlabeled documents and shows that this method performs in many cases perform better than others methods.
> >
> > **Notes :** 
> > - I think the proof of convergence is missing a few steps.
> > - I think the comparison with SVM did not use the right parameters, but that would be a further work in producing the article.

### week 31/07 to 04/08
> - worked in the WVIS paper
> - read first chapter of text mining book
> - read part of Thiago Theses
> - request inclusion of the discipline: complex network mining
