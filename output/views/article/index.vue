<template>
    <div class="app-container">
        <y-form
                ref="articleForm"
                :model="articleForm"
                label-width="80px"
        >
            <el-row type="flex" justify="end">
                <el-form-item>
                    <el-button type="success" @click="add">添加图文模块</el-button>
                </el-form-item>
            </el-row>


            
            
            
            <el-row type="flex" justify="space-between">
                <el-col :span="20">
                    <el-row>

                        
                        
                        <el-col :span="6">
                            <el-form-item label="标题:" prop="title">

                                
                                
                                <y-input
                                
                                v-model="articleForm.title"
                                
                                
                                
                                
                                
                                

                                />
                            </el-form-item>
                        </el-col>
                        
                        
                        
                        
                        
                        
                        
                        <el-col :span="6">
                            <el-form-item label="作者:" prop="author">

                                
                                
                                <y-input
                                
                                v-model="articleForm.author"
                                
                                
                                
                                
                                
                                

                                />
                            </el-form-item>
                        </el-col>
                        
                        
                        
                        
                        
                        
                        
                        <el-col :span="6">
                            <el-form-item label="栏目ID:" prop="catalog_id">

                                
                                
                                <y-select
                                
                                v-model="articleForm.catalog_id"
                                
                                 api="/api/catalogs" 
                                
                                
                                
                                

                                />
                            </el-form-item>
                        </el-col>
                        
                        

                    </el-row>
                </el-col>
                <el-col :span="4">
                    <el-row type="flex" justify="end">
                        <el-form-item>
                            <el-button type="primary" @click="onSearch">查询</el-button>
                            <el-button @click="reset" class="no-margin">重置</el-button>
                        </el-form-item>
                    </el-row>
                </el-col>
            </el-row>
            

        </y-form>

        <y-table :data="articlesData" :pagination="pagination" @sortBy="sortBy" @changePage4List="getList">
            <template>

                
                    
                        <el-table-column prop="title" label="标题"
                                         
                                         
                                          >

                        
                        
                        </el-table-column>
                    
                
                    
                
                    
                
                    
                        <el-table-column prop="author" label="作者"
                                         
                                         
                                          >

                        
                        
                        </el-table-column>
                    
                
                    
                        <el-table-column prop="is_header" label="首页头条"
                                          sortable="is_header" 
                                          width="100px" 
                                           align='center'   >

                        
                        
                            <template slot-scope="scope">
                                <el-button :type="scope.row.is_header? 'success':'info'" :icon="scope.row.is_header? 'el-icon-check':'el-icon-close'" circle ></el-button>
                            </template>
                        
                        </el-table-column>
                    
                
                    
                        <el-table-column prop="is_col_header" label="栏目显示"
                                          sortable="is_col_header" 
                                          width="100px" 
                                           align='center'   >

                        
                        
                            <template slot-scope="scope">
                                <el-button :type="scope.row.is_col_header? 'success':'info'" :icon="scope.row.is_col_header? 'el-icon-check':'el-icon-close'" circle ></el-button>
                            </template>
                        
                        </el-table-column>
                    
                
                    
                        <el-table-column prop="catalog_id" label="栏目ID"
                                         
                                          width="100px" 
                                           align='center'   >

                        
                        
                        </el-table-column>
                    
                



                <el-table-column label="操作" width="100px">
                    <template slot-scope="{row}">
                        <el-button type="text" size="small" @click="edit(row.id)">修改</el-button>
                        <el-button type="text" size="small" @click="del(row.id)">删除</el-button>
                    </template>
                </el-table-column>
            </template>
        </y-table>
    </div>
</template>
<script>
    import {getArticles, delArticle} from "@/api/article"

    export default {
        data() {
            return {
            articleForm: {},
            articlesData: [],
                pagination: {
                pageNumber: 1,
                    pageSize: 10
            },
            
        }
        },
        created() {
            this.getList()
        },
        methods: {
            async getList(param) {
                const response = await getArticles(
                    {
                        ...param,
                        page: this.pagination.pageNumber,
                        pagesize: this.pagination.pageSize
                    }
                )
                this.articlesData = response.data.list
                this.pagination.total = parseInt(response.data.pagination.total, 10)
            },

            add() {
                this.$router.push({path: "add"})
            },
            edit(id) {
                this.$router.push({path: "edit", query: {id}})
            },
            del(id) {
                this.$confirm("是否删除?", "提示", {
                    confirmButtonText: "确定",
                    cancelButtonText: "取消",
                    type: "warning"
                })
                    .then(() => {
                        delArticle(id).then((response) => {
                            this.$message({
                                type: "success",
                                message: "删除成功!"
                            })
                            this.getList()
                        })
                    })
                    .catch(() => {
                        this.$message({
                            type: "info",
                            message: "已取消删除"
                        })
                    })
            },
            onSearch(sort) {
                this.getList({...this.articleForm, ...sort})
            },
            sortBy(e) {
                this.onSearch(e)
            },
            reset() {
                this.articleForm = {}
                this.getList()
            }
        }
    }
</script>

<style lang='scss' scope>
    .app-container {
        padding: 20px;
        .no-margin{
            margin: 0;
        }
    }
</style>