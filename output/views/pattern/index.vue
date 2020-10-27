<template>
    <div class="app-container">
      <el-card>
        <div slot="header">
          <span>搜索条件</span>
        </div>
        <y-form
                ref="patternForm"
                :model="patternForm"
                label-width="80px"
        >

            
            
            
                    <el-row>

                        
                        
                        <el-col :span="6">
                            <el-form-item label="图案名称:" prop="name">

                                
                                
                                <y-input
                                
                                v-model="patternForm.name"
                                
                                
                                
                                
                                
                                

                                
                                

                                />
                            </el-form-item>
                        </el-col>
                        
                        
                        
                        

                    </el-row>

            

          <el-row type="flex" align="space-between">
            <el-col>
                <el-button type="primary" @click="onSearch">查询</el-button>
                <el-button @click="reset" class="y-mr-l-10">重置</el-button>
            </el-col>
            <el-button type="success" @click="add">添加图案</el-button>

          </el-row>
        </y-form>
      </el-card>
        <y-table :data="patternsData" :pagination="pagination" @sortBy="sortBy" @changePage4List="getList">
            <template>

                
                    
                        <el-table-column prop="name" label="图案名称"
                                         
                                         
                                          >

                        
                        
                        </el-table-column>
                    
                
                    
                        <el-table-column prop="pic" label="图案图片"
                                         
                                         
                                          >

                        
                        
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
    import {getPatterns, delPattern} from "@/api/pattern"

    export default {
        data() {
            return {
            patternForm: {},
            patternsData: [],
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
                const response = await getPatterns(
                    {
                        ...param,
                        page: this.pagination.pageNumber,
                        pagesize: this.pagination.pageSize
                    }
                )
                this.patternsData = response.data.list
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
                        delPattern(id).then((response) => {
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
                this.getList({...this.patternForm, ...sort})
            },
            sortBy(e) {
                this.onSearch(e)
            },
            reset() {
                this.patternForm = {}
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