<template>
    <div class="app-container">
      <el-card>
        <y-form
                ref="goodfabricForm"
                :model="goodfabricForm"
                label-width="80px"
        >

            
            
            
            
            
                    <el-row>

                        
                        
                        
                        
                        <el-col :span="6">
                            <el-form-item label="面料名称:" prop="name">

                                
                                
                                <y-input
                                
                                v-model="goodfabricForm.name"
                                
                                
                                
                                
                                
                                

                                
                                

                                />
                            </el-form-item>
                        </el-col>
                        
                        
                        
                        

                    </el-row>

            

          <el-row type="flex" align="space-between">
            <el-col>
                <el-button type="primary" @click="onSearch">查询</el-button>
                <el-button @click="reset" class="y-mr-l-10">重置</el-button>
            </el-col>
            <el-button type="success" @click="add">添加面料名称</el-button>

          </el-row>
        </y-form>
      </el-card>
        <y-table
            :data="goodfabricsData"
            :pagination="pagination"
            @sortBy="sortBy"
            @changePage4List="getList"
            class="y-p-t-20"
        >
            <template>

                
                    
                        <el-table-column prop="category"
                                         label="面料类别"
                                         align="center"
                                         
                                         
                                          >

                        
                        
                        </el-table-column>
                    
                
                    
                        <el-table-column prop="name"
                                         label="面料名称"
                                         align="center"
                                         
                                         
                                          >

                        
                        
                        </el-table-column>
                    
                
                    
                        <el-table-column prop="fabric_alias"
                                         label="面料别名"
                                         align="center"
                                         
                                         
                                          >

                        
                        
                        </el-table-column>
                    
                



                <el-table-column label="操作" width="100px"  align="center">
                    <template slot-scope="{row}">
                        <el-button type="text" size="small" @click="edit(row.id)">修改</el-button>
                      <el-divider direction="vertical"></el-divider>
                      <el-button type="text" size="small" @click="del(row.id)">删除</el-button>
                    </template>
                </el-table-column>
            </template>
        </y-table>
    </div>
</template>
<script>
    import {getGoodfabrics, delGoodfabric} from "@/api/goodfabric"

    export default {
        data() {
            return {
            goodfabricForm: {},
            goodfabricsData: [],
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
                const {data} = await getGoodfabrics(
                    {
                        ...param,
                        page: this.pagination.pageNumber,
                        pagesize: this.pagination.pageSize
                    }
                )
                this.goodfabricsData = data.list
                this.pagination.total = data.pagination.total
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
                        delGoodfabric(id).then((response) => {
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
                this.getList({...this.goodfabricForm, ...sort})
            },
            sortBy(e) {
                this.onSearch(e)
            },
            reset() {
                this.goodfabricForm = {}
                this.getList()
            }
        }
    }
</script>

<style lang='scss' scoped>
.app-container {

}
</style>