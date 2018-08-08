#include<bits/stdc++.h>
using namespace std;

typedef struct node{
	int id;
	struct node *left;
	struct node *right;
}NODE;

void preorder(NODE *root,vector<int> &pre){
	if(root!=NULL){
		pre.push_back(root->id);
		preorder(root->left,pre);
		preorder(root->right,pre);
	}
}

void postorder(NODE *root,vector<int> &post){
	if(root!=NULL){
		postorder(root->left,post);
		postorder(root->right,post);
		post.push_back(root->id);
	}
}
//Disjoint set
void initialize(int Arr[ ], int N){
    for(int i=0;i<N;i++){
    	Arr[i]=i ;
    }
}

int root(int Arr[ ],int i){
    while(Arr[ i ] != i){
     i = Arr[ i ];
    }
    return i;
}
void Union(int Arr[ ] ,int A ,int B,int n){
    int root_A = root(Arr, A);       
    int root_B = root(Arr, B);  
    Arr[ root_B ] = root_A ;
    for(int i=0;i<n;i++){
    	if(Arr[i]==root_B){
    		Arr[i]=root_A;
    	}
    }       //setting parent of root(B) as root(A).
}
// bool find(int A,int B){
//     if( root(A)==root(B) ){       //if A and B have same root,means they are connected.
//     	return true;
//     }
//     else{
//     	return false;
//     }
// }

int main(){
	int t;
	FILE *f = fopen("ethan_traverses_a_tree.txt","r");
	fscanf(f,"%d",&t);
	//cin>>t;
	for(int z=1;z<=t;z++){
		int n,k;
		fscanf(f,"%d %d",&n,&k);
		//cin>>n>>k;
		vector<NODE*> arr;
		for(int i=0;i<n;i++){
			NODE *node=new NODE;
			node->left=NULL;
			node->right=NULL;
			node->id=i;
			arr.push_back(node);
		}
		for(int i=0;i<n;i++){
			int a,b;
			fscanf(f,"%d %d",&a,&b);
			//cin>>a>>b;
			a--;b--;
			if(a>=0){
				arr[i]->left=arr[a];
			}
			if(b>=0){
				arr[i]->right=arr[b];
			}
		}
		NODE *root=arr[0];
		vector<int> pre,post;
		preorder(root,pre);
		postorder(root,post);
		// for(int i=0;i<pre.size();i++){
		// 	cout<<pre[i]<<" ";
		// }
		// cout<<endl;
		// for(int i=0;i<post.size();i++){
		// 	cout<<post[i]<<" ";
		// }
		// cout<<endl;
		
		int Arr[n];
		initialize(Arr,n);
		for(int i=0;i<n;i++){
			Union(Arr,pre[i],post[i],n);
		}
		// for(int i=0;i<n;i++){
		// 	cout<<Arr[i]+1<<" ";
		// }
		// cout<<endl;
		set <int> s{Arr,Arr+n};
		//cout<<s.size()<<endl;
		FILE *fp=fopen("output.txt","a");
		if(k>s.size()){
			fprintf(fp, "Case #%d: ",z);
			fprintf(fp,"Impossible\n");
		}
		else{
			int counter=1;
			int *labels=new int[n];
			for(int i=0;i<n;i++){
				int curr=Arr[i];
				if(curr!=-1){
					Arr[i]=-1;
					labels[i]=counter;
					for(int j=i+1;j<n;j++){
						if(Arr[j]==curr){
							Arr[j]=-1;
							labels[j]=counter;
						}
					}
					if(counter<k){counter++;}
				}
				
			}
		fprintf(fp, "Case #%d:",z);
		for(int i=0;i<n;i++){
			fprintf(fp," %d",labels[i]);
		}
		fprintf(fp, "\n");
		}
		fclose(fp);

	}
	fclose(f);
	return 0;
}