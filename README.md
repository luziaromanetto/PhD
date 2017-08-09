# PhD

### TODO list:
> - read the paper *Optimizing the class information divergence for transductive classification of texts using propagation in bipartite graphs*
> - read the unpublished paper
> - talk with Alneu about the project.
> - look for a image dataset to test the Alneu idea of thest the PBG in this context.   

## week 07/08 to 11/08
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
