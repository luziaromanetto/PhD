# PhD

### TODO list:
> - read the rossi new paper, to understand the cost function in the other paper;
> - talk with Alneu about the project;
> - see the paper in tidea;

## week 21/08 to 25/08
> - writing the new project;
> - choosing the paper for the lecture;
> - Finish code for BG;
> > Good results
> - read the unpublished paper;
  
## week 14/08 to 18/08

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


## week 07/08 to 11/08
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

## week 31/07 to 04/08
> - worked in the WVIS paper
> - read first chapter of text mining book
> - read part of Thiago Theses
> - request inclusion of the discipline: complex network mining
