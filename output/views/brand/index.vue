<template>
    <div class="app-container">
      <el-card>
        <div slot="header">
          <span>搜索条件</span>
        </div>
        <y-form
                ref="brandForm"
                :model="brandForm"
                label-width="80px"
        >

            
            
            
                    <el-row>

                        
                        
                        <el-col :span="6">
                            <el-form-item label="品牌名称:" prop="brand">

                                
                                
                                <y-input
                                
                                v-model="brandForm.brand"
                                
                                
                                
                                
                                
                                

                                
                                

                                />
                            </el-form-item>
                        </el-col>
                        
                        

                    </el-row>

            

          <el-row type="flex" align="space-between">
            <el-col>
                <el-button type="primary" @click="onSearch">查询</el-button>
                <el-button @click="reset" class="y-mr-l-10">重置</el-button>
            </el-col>
            <el-button type="success" @click="add">添加品牌</el-button>

          </el-row>
        </y-form>
      </el-card>
        <y-table :data="brandsData" :pagination="pagination" @sortBy="sortBy" @changePage4List="getList">
            <template>

                
                    
                        <el-table-column prop="brand" label="品牌名称"
                                         
                                         
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
    import {getBrands, delBrand} from "@/api/brand"

    export default {
        data() {
            return {
            brandForm: {},
            brandsData: [],
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
                const response = await getBrands(
                    {
                        ...param,
                        page: this.pagination.pageNumber,
                        pagesize: this.pagination.pageSize
                    }
                )
                this.brandsData = response.data.list
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
                        delBrand(id).then((response) => {
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
                this.getList({...this.brandForm, ...sort})
            },
            sortBy(e) {
                this.onSearch(e)
            },
            reset() {
                this.brandForm = {}
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